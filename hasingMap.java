import java.util.HashMap;
import java.util.Scanner;
public class hasingMap {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i =0;i<n;i++){
            arr[i]=scanner.nextInt();
            map.put(arr[i], map.getOrDefault(arr[i],0)+1);
        }
        System.out.println("How many numbers want to check : ");
        int x = scanner.nextInt();
        while(x-- > 0){
            int number = scanner.nextInt();
            System.out.println("Count for number "+number+" is "+map.getOrDefault(number,0));
        }
        scanner.close();
    }
    
}
