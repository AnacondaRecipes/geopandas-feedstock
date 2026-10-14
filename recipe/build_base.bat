REM GitHub archive has no .git; hatch-vcs needs a pretend version.
set SETUPTOOLS_SCM_PRETEND_VERSION=%PKG_VERSION%
set HATCH_VCS_PRETEND_VERSION=%PKG_VERSION%
%PYTHON% -m pip install . --no-deps --no-build-isolation -vv
if errorlevel 1 exit 1