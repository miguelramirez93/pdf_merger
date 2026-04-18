# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for PDF Merger

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('merger', 'merger'),
        ('dir', 'dir'),
        ('infrastructure', 'infrastructure'),
        ('shared', 'shared'),
        ('README.md', '.'),
        ('CHANGELOG.md', '.'),
        ('LICENSE', '.'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=[],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='pdf_merger',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
