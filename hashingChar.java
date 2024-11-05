import java.util.Scanner;
public class hashingChar {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String s = scanner.next().toLowerCase();
        int hash[] = new int[26];
        for(int i =0;i<s.length();i++){
            char c = s.charAt(i);
            hash[c-'a']++;
            
        }
        System.out.println("How many Characters you want to match : ");
        int n = scanner.nextInt();
        while(n-- >0){
            char ch = scanner.next().charAt(0);
            if(ch>='a' && ch<='z'){
                System.out.println(hash[(int)ch - 'a']);
            }
            else{
                System.out.println("Input not valid");
            }

        }

        scanner.close();    
    }
}
