import cmd, os, fileinput, shutil



class InitProject(cmd.Cmd):

    def do_init(self, project_name):
        print ' [x] Preparing %s project.' % project_name
        if not self.good_directory():
            raise Exception('You must run this script from project directory : ' + os.path.split(__file__)[0])


        self.walk_in_directories(os.getcwd(), project_name)
        print ' [x] Done'

    def rreplace(self, s, old, new, occurrence):
        li = s.rsplit(old, occurrence)
        return new.join(li)


    def walk_in_directories(self, directories, project_name):
        lower = project_name.lower()
        for root, dirs, files in os.walk(directories, topdown=False):

            for f in files:
                # replace occurence of 'turbotequila' in files
                if f.endswith('.py'):
                    for line in fileinput.FileInput(os.path.join(root, f), inplace=1):
                        print line.replace('turbotequila', lower)

                # replace filenames with 'turbotequila'
                f = f.replace('turbotequila', lower)

            # if path ends with 'turbotequila', replace it
            if os.path.split(root)[1].count('turbotequila') >= 1:
                tmp = self.rreplace(root, 'turbotequila', lower, 1)
                shutil.move(root, tmp)


    def good_directory(self):
        """
        Verify that the script is launched from the right directory
        """
        return os.path.split(os.path.abspath(__file__))[0] == os.getcwd()



    def do_EOF(self, line):
        return False


if __name__ == '__main__':
    import sys
if len(sys.argv) > 1:
    InitProject().onecmd('init ' + sys.argv[1])
else:
    print '''
    Enter the name of your project as first argument (with no withespaces):
    $python %s <myNewProject>.
        ''' % os.path.split(__file__)[1]