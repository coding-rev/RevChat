from os import system

def link():
    main()

def Index(username):
    print('Hello', username,"\t\tpress 'r' for refresh")
    print("\tYour Chat")
    print('-----------------------------------')
    infile=open('__all__.txt','r')
    content=infile.read()
    infile.close()
    edit_content=content.replace(username,'')
    main_edit_content=edit_content.replace(' ','')
    print(main_edit_content)
    talk=input('Type friends name : ')
    system('cls')
    if talk=='r':
        Index(username)

    else:
        print('''Tips :
'0' for Back
'r' for refresh
'cc' to clear chat
'00' for change user
---------------------------------------------------''')
        
        try:
            
            friend=open(username+'.txt','r')
            words=friend.read()
            friend.close()
            print('To :',talk)
            print(words)
            while True:
                
                print(' ')
                sms=input("type message : "  )
                system('cls')
                #'r' for refresh option
                if sms=='r':
                    system('cls')
                    refresh=open(username+'.txt','r')
                    inside=refresh.read()
                    print('To :',talk)
                    print(inside)
                #'0' Back to chat list
                elif sms=='0':
                    system('cls')
                    print('loading previous page .....please wait')
                    system('pause')
                    Index(username)
                elif sms=='00':
                    system('cls')
                    print('changing user..... please wait')
                    system('pause')
                    link()
                #'clear_chat' or 'cc' to clear chat
                elif sms=='cc':
                    print('Are you sure you want to clear You and',talk,"'s Chat?")
                    print('Y | N')
                    yes_no=input().lower()
                    if yes_no=='y':
                        delete_me=open(username+'.txt','w')
                        delete_me.write(' ')
                        delete_me.close()
                        print('Chat deleted successfully')
                        system('pause')
                        Index(username)
                    elif yes_no=='n':
                        print('Command Aborted')
                        system('pause')
                        Index(username)
                    
                # for messages    
                else:
                
                    talking=open(talk+'.txt','a')
                    talking.write('\n')
                    talking.write(username)
                    talking.write(' : ')
                    talking.write(sms)
                    talking.close()

                    talk_me=open(username+'.txt','a')
                    talk_me.write('\n')
                    talk_me.write('Me ')
                    talk_me.write(': ')
                    talk_me.write(sms)
                    talk_me.close()
                    system('cls')
                    me=open(username+'.txt', 'r')
                    insider=me.read()
                    print('To :',talk)
                    print(insider)
                    me.close()

            
        except:
            print('Entered name not found')
            print('0.back')
            backback=input()
            system('cls')
            if backback=='0':
                Index(username)
            else:
                print('Server Timeout')
                system('brk')
            
            
    

    
def main():
    print('welcome to RevApp')
    print('1. Signup     2.Login ')
    login=input()
    system('cls')
    if login=='1':
        print('\tSignup')
        print(' ')
        username=input('Username : ')
        edit_username=username.replace(' ','')
        print(' ')
        password1=input('Password : ')
        print(' ')
        password2=input('Confirm Password : ')
        print(' ')
        print("press '1' or Type 'create'")
        submit=input()
        system('cls')
        name=edit_username+'.txt'
        if submit=='1' or 'create':
            if password1==password2:
                userfile=open(name,'w')
                userfile.write(username)
                userfile.write(password1)
                #close the file
                userfile.close()
                infile=open('__all__.txt','a')
                infile.write('\n')
                infile.write(username)
                infile.write('\n')
                infile.write('-------------------------------------')
                infile.close()
          
                Index(username)
            else:
                print("Inputs didn't match | Check passwords well")
                print("0. Back")
                back=input()
                system("cls")
                if back=='0':
                    main()
                else:
                    system("brk")

    elif login=='2':
        print('\tLogin')
        print(' ')
        username=input("Username : ")
        edit_username=username.replace(' ','')
        print(' ')
        password=input("Password : ")
        system('cls')
        try:
            result=edit_username+'.txt'
            infile = open(result,'r')
            content=infile.read()
            infile.close()

            if password in content:
                Index(username)

            else:
                print("Password didn't match User")
                print('0. Back')
                Back=input()
                if Back=='0':
                    main()
                else:
                    system('brk')

            
        except:
            print("User name does not exist")
            print("Server Timeout")
            print('0. Back')
            back=input()
            system('cls')
            if back=='0':
                main()
            else:
                system('brk')

    else:
        
        print('Shine your eyes bro...hihi')
        print('0. Back')
        backwards=input()
        system('cls')
        if backwards=='0':
            main()
        else:
            print("Server Timeout")
            system('brk')
            
        

main()
