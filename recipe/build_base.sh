# GitHub archive has no .git; hatch-vcs needs a pretend version.
export SETUPTOOLS_SCM_PRETEND_VERSION="${PKG_VERSION}"
export HATCH_VCS_PRETEND_VERSION="${PKG_VERSION}"
${PYTHON} -m pip install . --no-deps --no-build-isolation -vv
