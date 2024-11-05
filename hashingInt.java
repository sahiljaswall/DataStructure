import java.util.Scanner;
public class hashingInt {
    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i]=scanner.nextInt();
        }

        int[] hash= new int[13];
        for(int i =0;i<n;i++){
            if(arr[i] < hash.length){
                hash[arr[i]] +=1;

            }
            }
        int m = scanner.nextInt();
        while(m-- >0){
            int number =scanner.nextInt();
            if (number>=0 && number <hash.length){
                System.out.println(hash[number]);
            } else{
                System.out.println("Number out of range");
            }
        }
        scanner.close();
    }
}
