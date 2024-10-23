Simple test package

# Reminder for me: build and distribute package

# pip install build

# PEP 517 and PEP 518:
# don't use setup.py any more , use pyproject.toml with, for example, 
# [build-system]
# requires = ["setuptools>=42", "wheel"]
# build-backend = "setuptools.build_meta"

# python -m build
# this creates tst_pckg-0.1-py3-none-any.whl
# I can now install the package, 
# pip install dist/tst_pckg-0.1-py3-none-any.whl

# make it a git repo and send it to 
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/VesaApaja/tst_pckg.git
git push -u origin main