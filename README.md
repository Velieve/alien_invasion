# alien_invasion

Git跟踪是谁修改了项目，哪怕参与项目开发的人只有一个。为此，Git需要知道你的用户名和电子邮箱地址。你必须提供用户名，但可使用虚构的电子邮箱地址：


`` $ git config --global user.name "_username_" ``

`` $ git config --global user.email "_username@example.com_" ``

前面创建了一个目录，其中包含一个Python文件和一个.gitignore文件，现在可以初始化一个Git仓库了。为此，打开一个终端窗口，切换到文件夹git_practice，并执行如下命令：


`` git_practice$ git init ``
`` Initialized empty Git repository in git_practice/.git/ ``


输出表明Git在git_practice中初始化了一个空仓库。仓库 是程序中被Git主动跟踪的一组文件。Git用来管理仓库的文件都存储在隐藏的目录.git中，你根本不需要与这个目录打交道，但千万不要删除它，否则将丢失项目的所有历史记录。