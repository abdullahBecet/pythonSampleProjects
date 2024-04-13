import socket

def portScanner(targetHost,targetPort):
    for port in targetPort:
        try:
            soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            soc.settimeout(1)
            result=soc.connect_ex((targetHost,port))

            if result == 0:
                print(f"Port {port} is open")
                
            else:
                print(f"Port {port} is close")
                

            soc.close()
        
        except KeyboardInterrupt:
            print("Log is exist")

        except socket.error:
            print("Connection is break")
            break

targetHost= " " #Write Your Host
targetPort=[80,8080,23,22,21,3389,95,93,995,444,443]

portScanner(targetHost,targetPort)