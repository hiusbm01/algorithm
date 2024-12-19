import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());

        num /= 100;
        num *= 100;
        int f = Integer.parseInt(br.readLine());
        int a = 0;
        while(num % f != 0){
            num++;
            a++;
        }
        if(a < 10){
            System.out.println("0"+a);
        }else{
            System.out.println(a);
        }
    }
}
