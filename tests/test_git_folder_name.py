import os

from pyfakefs.fake_filesystem import FakeFilesystem

from conf_utils import git_folder_name


def test_no_git_folder(fs: FakeFilesystem):
    fs.create_dir("/home/user/project/")
    os.chdir("/home/user/project")

    assert git_folder_name() is None


def test_git_folder_here(fs: FakeFilesystem):
    fs.create_dir("/home/user/project/.git/")
    os.chdir("/home/user/project")

    assert git_folder_name() == "project"


def test_git_folder_parent(fs: FakeFilesystem):
    fs.create_dir("/home/user/project/")
    fs.create_dir("/home/user/.git/")
    os.chdir("/home/user/project")

    assert git_folder_name() == "user"


def test_git_folder_root(fs: FakeFilesystem):
    fs.create_dir("/home/user/project/")
    fs.create_dir("/.git/")
    os.chdir("/home/user/project")

    assert git_folder_name() == ""


def test_git_folder_other(fs: FakeFilesystem):
    fs.create_dir("/home/user/project/")
    os.chdir("/home/user/project")

    fs.create_dir("/home/user/another_project/.git/")

    assert git_folder_name("/home/user/another_project/") == "another_project"
