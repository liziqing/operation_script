# -*- coding: utf-8 -*-
import sys
import getopt

class Pysys(object):
    
    log_path = ''

    def usage(self):
        print 'PyTest.py usage:'
        print '-h,--help: print help message.'
        print '-V, --version: print script version'
        print '-l, --log_path: log dir path'
    def version(self):
        print 'PyTest.py 1.0.0.0.1'
    def outPut(self, args):
        print 'Hello, %s'%args
    def main(self, argv):
        longopts = ['help=', 'version=', 'log_path=']
        args_permission = 'hvl:'
        if len(argv[1:]) == 0:
            print "####################################"
            print "             WARNING!"
            print "####################################\n"
            print "please specify a log directory using '-l' or '--log_path'!\n\n"
            print "using '-h' or '--help' to get help info!"
            sys.exit(1)
        try:
            opts, args = getopt.getopt(argv[1:], args_permission, longopts)
        except getopt.GetoptError, err:
            print str(err)
            self.usage()
            sys.exit(1)
        for o, a in opts:
            if o in ('-h', '--help'):
                self.usage()
                sys.exit(1)
            elif o in ('-v', '--version'):
                self.version()
                sys.exit(0)
            elif o in ('-o', '--output'):
                self.outPut(a)
                sys.exit(0)
            elif o in ('-l', '--log_path',):
                log_path = a
                return log_path
            else:
                print 'unhandled option'
                sys.exit(3)