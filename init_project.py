import cmd, os



class InitProject(cmd.Cmd):

    def do_init(self, project_name):
        print ' [x] Preparing %s project.' % project_name
        if not self.good_directory():
            raise Exception('You must run this script from project directory : %s' % os.path.split(__file__)[0])


        self.walk_in_directories(os.getcwd())



    def walk_in_directories(self, directories):
        for root, dirs, files in os.walk(directories, topdown=True):
            print root, dirs, files

    def good_directory(self):
        """
        Verify that the script is launched from the right directory
        """
        return os.path.split(__file__)[0] == os.getcwd()



    def do_EOF(self, line):
        return False

    def postloop(self):
        print 'ended'



if __name__ == '__main__':
    import sys
if len(sys.argv) > 1:
    InitProject().onecmd('init ' + sys.argv[1])
else:
    print '''
    Enter the name of your project as first argument (with no withespaces):
    $python %s <myNewProject>.
        ''' % os.path.split(__file__)[1]