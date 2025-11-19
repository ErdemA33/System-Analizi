[Setup]
AppName=System Inspector & Cleaner
AppVersion=1.0
DefaultDirName={pf}\System Inspector Cleaner
DefaultGroupName=System Inspector Cleaner
OutputDir=output
OutputBaseFilename=SystemInspectorInstaller
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Files]
Source: "..\ui\dist\app.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\ui\dist\logs\*"; DestDir: "{app}\logs"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{userdesktop}\System Inspector & Cleaner"; Filename: "{app}\app.exe"
Name: "{group}\System Inspector & Cleaner"; Filename: "{app}\app.exe"

[Run]
Filename: "{app}\app.exe"; Description: "Uygulamayý baþlat"; Flags: nowait postinstall runasoriginaluser
