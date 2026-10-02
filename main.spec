# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['E:/hello world/Python Courses/New Course 2025/Projects/Project 11/interactive_gui.py'],
    pathex=[],
    binaries=[],
    datas=[('E:/hello world/Python Courses/New Course 2025/Projects/Project 11/irregular_verbs_list.csv', '.'), ('E:/hello world/Python Courses/New Course 2025/Projects/Project 11/main.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='SentenceTransformation-v1.0',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
