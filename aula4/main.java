package aula4;

// parte a rastrear duas funcoes recursivas na mao entregando a pilha desenhada
// parte b implementar tres funcoes recursivas: soma de vetor, inverter texto e torre de hanoi
// parte c instrumentar o fibonacci recursivo contando as chamadas e explicar por que ele nao escala

public class main {
    static int some(int n){
        if (n == 0) {
            return 0;
        } else {
            return n + some(n - 1);
        }
    }

    // mesma recursao, mas imprimindo cada passo ao desempilhar as chamadas
    static int someComTraco(int n) {
        if (n == 0) {
            System.out.println("some(0) = 0");
            return 0;
        }
        int resultado = n + someComTraco(n - 1);
        System.out.println("some(" + n + ") = " + n + " + some(" + (n - 1) + ") = " + resultado);
        return resultado;
    }

    static int[] v = {1, 2, 3, 4, 5};

    static int maior(int[] v) {
        int m = v[0];
        for (int i = 1; i < v.length; i++) {
            if (v[i] > m) {
                m = v[i];
            }
        }
        return m;
    }

    static int f(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * f(n - 1);
        }
    }

    static int q(int n) {
        if (n == 0) {
            return 0;
        } else {
            return f(n) + q(n - 1);
        }
    }

    // ===== parte a: rastrear a pilha de chamadas =====
    // cada "entra" empilha um quadro, cada "sai" desempilha; a indentacao mostra
    // a profundidade da pilha naquele instante -- usar essa saida como base para
    // desenhar a pilha a mao (cada linha "entra" e um quadro empilhado)
    static int someRastreado(int n, int profundidade) {
        System.out.println("  ".repeat(profundidade) + "entra some(" + n + ")");
        int resultado = (n == 0) ? 0 : n + someRastreado(n - 1, profundidade + 1);
        System.out.println("  ".repeat(profundidade) + "sai   some(" + n + ") = " + resultado);
        return resultado;
    }

    static int fRastreado(int n, int profundidade) {
        System.out.println("  ".repeat(profundidade) + "entra f(" + n + ")");
        int resultado = (n == 0) ? 1 : n * fRastreado(n - 1, profundidade + 1);
        System.out.println("  ".repeat(profundidade) + "sai   f(" + n + ") = " + resultado);
        return resultado;
    }

    // ===== parte b: tres funcoes recursivas =====
    static int somaVetor(int[] v, int i) {
        if (i == v.length) {
            return 0;
        }
        return v[i] + somaVetor(v, i + 1);
    }

    static String inverterTexto(String s) {
        if (s.length() <= 1) {
            return s;
        }
        return inverterTexto(s.substring(1)) + s.charAt(0);
    }

    static void hanoi(int n, char origem, char destino, char auxiliar) {
        if (n == 0) {
            return;
        }
        hanoi(n - 1, origem, auxiliar, destino);
        System.out.println("mover disco " + n + " de " + origem + " para " + destino);
        hanoi(n - 1, auxiliar, destino, origem);
    }

    // ===== parte c: fibonacci recursivo instrumentado =====
    static int chamadasFibonacci = 0;

    static int fibonacci(int n) {
        chamadasFibonacci++;
        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {
        System.out.println("=== recursao basica ===");
        System.out.println(some(3));

        System.out.println();
        someComTraco(3);

        System.out.println();
        System.out.println("maior(v) = " + maior(v));

        System.out.println();
        System.out.println("q(3) = " + q(3));

        System.out.println();
        System.out.println("=== parte a: pilha de chamadas ===");
        System.out.println("-- some(3) --");
        someRastreado(3, 0);
        System.out.println("-- f(3) --");
        fRastreado(3, 0);

        System.out.println();
        System.out.println("=== parte b: tres funcoes recursivas ===");
        System.out.println("somaVetor(v) = " + somaVetor(v, 0));
        System.out.println("inverterTexto(\"recursao\") = " + inverterTexto("recursao"));
        System.out.println("hanoi(3 discos):");
        hanoi(3, 'A', 'C', 'B');

        System.out.println();
        System.out.println("=== parte c: fibonacci recursivo instrumentado ===");
        for (int n : new int[] {10, 20, 30}) {
            chamadasFibonacci = 0;
            long inicio = System.nanoTime();
            int resultado = fibonacci(n);
            long tempoMs = (System.nanoTime() - inicio) / 1_000_000;
            System.out.println("fibonacci(" + n + ") = " + resultado
                    + "  chamadas=" + chamadasFibonacci + "  tempo=" + tempoMs + "ms");
        }
        System.out.println("a cada +1 em n o numero de chamadas quase dobra (cresce em O(2^n)),");
        System.out.println("porque a recursao recalcula do zero os mesmos subproblemas em vez de");
        System.out.println("reaproveitar resultados ja obtidos -- por isso nao escala para n grande");
        System.out.println("sem memoization ou uma versao iterativa.");
    }
}
