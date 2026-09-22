package aula5;

public class main {
  
    static long chamadas = 0;

    static long fib(int n) {
        chamadas++;
        if (n <= 1) {
            return n;
        }
        return fib(n - 1) + fib(n - 2);
    }

    public static void main(String[] args) {
        int[] valores = {10, 20, 25, 30};
        for (int n : valores) {
            chamadas = 0;
            fib(n);
            System.out.printf("n = %2d | Chamadas: %10d%n", n, chamadas);
        }
    }
}

