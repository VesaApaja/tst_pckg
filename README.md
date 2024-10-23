# Simple test package

Reminder for me: build and distribute a package  
$ pip install build  

PEP 517 and PEP 518:  
don't use setup.py any more , use pyproject.toml with, for example,

 [build-system]
 requires = ["setuptools>=42", "wheel"]   
 build-backend = "setuptools.build_meta"  		

 $ python -m build  
 this creates tst_pckg-0.1-py3-none-any.whl  
 I can now install the package,  
 $pip install dist/tst_pckg-0.1-py3-none-any.whl  

Make it a git repo and send it to github  
$ git init  
$ git add .  
$ git commit -m "Initial commit"  
#ssh auth  
Login to github and setup ssh key authentication.
Then 
$ git remote set-url origin git@github.com/VesaApaja/tst_pckg.git

for https auth this would be  
$ git remote add origin https://github.com/VesaApaja/tst_pckg.git

$ git push -u origin main


$ git remote -v  
origin	https://github.com/VesaApaja/tst_pckg.git (fetch)  
origin	https://github.com/VesaApaja/tst_pckg.git (push)

$ ssh -T git@github.com
Hi VesaApaja! You've successfully authenticated, but GitHub does not provide shell access.

Login to your (my) gothub page and add a new repository tst_pckg

$ git push --set-upstream origin master

Enumerating objects: 24, done.  
Counting objects: 100% (24/24), done.  
Delta compression using up to 16 threads  
Compressing objects: 100% (21/21), done.  
Writing objects: 100% (24/24), 5.79 KiB | 5.79 MiB/s, done.  
Total 24 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)  
remote: Resolving deltas: 100% (2/2), done.  
To github.com:VesaApaja/tst_pckg.git  
 * [new branch]      master -> master  
branch 'master' set up to track 'origin/master'.  
