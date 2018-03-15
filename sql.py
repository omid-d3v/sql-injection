__author__ = 'Xboy'
import urllib




print "  }--------------{+} Coded By Xboy Hacker {+}--------------{"
print "           }--------{+}  it-teach.net {+}--------{"


while(True):
    target = raw_input("Enter Url Target:")
    if (target=="exit"):
        break;
    data = urllib.urlopen(target + '\'')
    R = data.read()
    if 'You have an error in your SQL syntax;' in R:
        print "[+] vulnerable"
    elif 'supplied argument is not a valid MySQL result resource in' in R:
        print "[+] vulnerable"
    elif 'check the manual that corresponds to your MySQL server version for the right syntax to use near' in R:
        print "[+] vulnerable"
    elif 'check the manual that corresponds to your MySQL server version for the right syntax to use near' in R:
        print "[+] vulnerable"
    else:
        print "[-] Not vulnerable"
