import java.util.Scanner;

public class SelectionSortAlgo {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i]=scanner.nextInt();
        }
        System.out.println("Orignal Array");
        for(int i=0;i<n;i++){
            System.out.print(arr[i]+" ");
        }
        for(int i=0; i<=n-2;i++){
            int mini =i;
            for(int j=i+1; j<=n-1;j++){
                if(arr[j]<arr[mini]){
                    mini = j;
                }
            }
            int temp = arr[i];
            arr[i]=arr[mini];
            arr[mini]=temp;
        }
        System.out.println("Updated Array");
        for(int i=0;i<n;i++){
            System.out.print(arr[i]+" ");
        }
    }    
}
