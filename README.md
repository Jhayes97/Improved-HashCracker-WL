# Improved-HashCracker-WL
Supports md5, sha1, ripe160md, sha256, sha512, NTLM, known salts, command line argument parsing.


#Syntax 


required arguments:

-t {md5,sha1,ripe160md,sha256,sha512,NTLM}, --Type {md5,sha1,ripe160md,sha256,sha512,NTLM}
                        The type of hash you would like.
-d <DICT>, --Dict <DICT>  The word list you will be using.

-hv <HASH>, --Hash <HASH>
                        The hash value to crack.
optional arguments:
  -h, --help            show this help message and exit
  
  
  -sp <PREFIX>, --Prefix <PREFIX>
                        The salt prefix to prepend.
 
  -ss SUFFIX, --Suffix <SUFFIX>
                        The salt suffix to append.

#Examples


$./MultiHashArg.py -t md5 -d /usr/share/wordlists/fasttrack.txt -hv d2bc2f8d09990ebe87c809684fd78c66 -sp 123
The password was: password
$

Made by James Hayes
