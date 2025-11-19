import psutil
import GPUtil
import platform
import time
import os
import shutil
import json
import winreg
from datetime import datetime

LOG_PATH = "logs/system_logs.json"


# ----------------------------------------------------
# CPU MODEL
# ----------------------------------------------------
def get_cpu_model():
    try:
        cpu = platform.processor()
        if cpu and cpu.strip():
            return cpu
    except:
        pass

    try:
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"HARDWARE\DESCRIPTION\System\CentralProcessor\0"
        )
        model, _ = winreg.QueryValueEx(key, "ProcessorNameString")
        return model
    except:
        return "Bilinmiyor"


# ----------------------------------------------------
# TEMP FOLDER UTILS
# ----------------------------------------------------
def get_folder_size(path):
    total = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            try:
                fp = os.path.join(root, f)
                total += os.path.getsize(fp)
            except:
                pass
    return total


def format_size(bytes_size):
    if bytes_size < 1024:
        return f"{bytes_size} B"
    kb = bytes_size / 1024
    if kb < 1024:
        return f"{kb:.2f} KB"
    mb = kb / 1024
    if mb < 1024:
        return f"{mb:.2f} MB"
    gb = mb / 1024
    return f"{gb:.2f} GB"


# ----------------------------------------------------
# GPU INFO
# ----------------------------------------------------
def get_gpu_info():
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return ("Bulunamadı", 0)
        g = gpus[0]
        load = max(0, min(100, g.load * 100))
        return (g.name, load)
    except:
        return ("Bulunamadı", 0)


# ----------------------------------------------------
# ANALİZ + TEMİZLE
# ----------------------------------------------------
def run_analysis(clean=False):
    log_text = "=== Sistem Analizi Başladı ===\n"

    # CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_phys = psutil.cpu_count(logical=False)
    cpu_log = psutil.cpu_count(logical=True)
    cpu_model = get_cpu_model()

    # RAM
    ram_usage = psutil.virtual_memory().percent

    # Disk
    disk_usage = psutil.disk_usage("C:\\").percent

    # GPU
    gpu_name, gpu_usage = get_gpu_info()

    # TEMP
    temp_path = os.environ.get("TEMP")
    temp_before = get_folder_size(temp_path)

    log_text += f"CPU: {cpu_usage}% | Fiziksel: {cpu_phys} | Mantıksal: {cpu_log}\n"
    log_text += f"GPU: {gpu_name} | Kullanım: {gpu_usage:.1f}%\n"
    log_text += f"RAM: {ram_usage}% | Disk: {disk_usage}%\n"
    log_text += f"TEMP klasörü: {format_size(temp_before)} (Temizleme öncesi)\n\n"

    deleted_files = []

    if clean:
        log_text += "TEMP klasörü temizleniyor...\n"

        try:
            for item in os.listdir(temp_path):
                fp = os.path.join(temp_path, item)
                try:
                    if os.path.isfile(fp):
                        os.remove(fp)
                        deleted_files.append(fp)
                    elif os.path.isdir(fp):
                        shutil.rmtree(fp, ignore_errors=True)
                        deleted_files.append(fp + "\\")
                except:
                    pass
        except:
            pass

        if deleted_files:
            log_text += "Silinen Dosyalar:\n"
            for f in deleted_files:
                log_text += f" - {f}\n"
        else:
            log_text += "Silinecek dosya bulunamadı.\n"

    temp_after = get_folder_size(temp_path)

    log_text += f"\nTEMP önce: {format_size(temp_before)} | sonra: {format_size(temp_after)}\n"
    log_text += "=== Sistem Analizi Bitti ===\n\n"

    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "log_text": log_text,
        "system_info": {
            "cpu": {
                "model": cpu_model,
                "usage_percent": cpu_usage,
                "cores_physical": cpu_phys,
                "cores_logical": cpu_log
            },
            "gpu": {"name": gpu_name, "usage_percent": gpu_usage},
            "ram": {"usage_percent": ram_usage},
            "disk": {"usage_percent": disk_usage},
        },
        "temp": {
            "temp_path": temp_path,
            "before_size_human": format_size(temp_before),
            "after_size_human": format_size(temp_after)
        }
    }

    save_log(entry)
    return entry


# ----------------------------------------------------
# KAYDET / OKU
# ----------------------------------------------------
def save_log(entry):
    os.makedirs("logs", exist_ok=True)
    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    data.append(entry)

    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_logs():
    if not os.path.exists(LOG_PATH):
        return []
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


__all__ = [
    "run_analysis",
    "load_logs",
    "get_folder_size",
    "format_size"
]
