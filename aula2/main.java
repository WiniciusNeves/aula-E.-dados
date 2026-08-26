// matriz de 4 linhas por 5 colunas achatada em um vetor
// 1) m[2][3] esta em qual posicao do vetor? 13
// 2) a posicao 13 do vetor e qual linha e qual coluna da matriz? 14

public class main {
    public static void main(String[] args) {
        int m[][] = {
                { 1, 2, 3, 4, 5 },
                { 6, 7, 8, 9, 10 },
                { 11, 12, 13, 14, 15 },
                { 16, 17, 18, 19, 20 }
        };
        int colunas = m[0].length;

        int i = 2;
        int j = 3;
        int posicaoVetor = i * colunas + j;
        System.out.println("m[" + i + "][" + j + "] = " + m[i][j] + " -> posicao " + posicaoVetor + " do vetor");

        int posicao = 13;
        int linha = posicao / colunas;
        int coluna = posicao % colunas;
        System.out.println("posicao " + posicao + " do vetor -> m[" + linha + "][" + coluna + "] = " + m[linha][coluna]);

        System.out.println();
        MultiplicacaoMatrizes.executar();

        System.out.println();
        MatrizEsparsa.executar();

        System.out.println();
        DensidadeComparacao.executar();
    }
}

// ordem dos lacos
// implementar a multiplicacao nas duas ordens (ijk e ikj)
// e medir/relatar o fator observado na sua maquina
class MultiplicacaoMatrizes {

    static int[][] multiplicarIJK(int[][] a, int[][] b) {
        int n = a.length, m = b[0].length, p = b.length;
        int[][] c = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int soma = 0;
                for (int k = 0; k < p; k++) {
                    soma += a[i][k] * b[k][j];
                }
                c[i][j] = soma;
            }
        }
        return c;
    }

    static int[][] multiplicarIKJ(int[][] a, int[][] b) {
        int n = a.length, m = b[0].length, p = b.length;
        int[][] c = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < p; k++) {
                int aik = a[i][k];
                for (int j = 0; j < m; j++) {
                    c[i][j] += aik * b[k][j];
                }
            }
        }
        return c;
    }

    static int[][] matrizAleatoria(int n, int m) {
        int[][] r = new int[n][m];
        java.util.Random rand = new java.util.Random(42);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                r[i][j] = rand.nextInt(10);
            }
        }
        return r;
    }

    static void executar() {
        System.out.println("=== Multiplicacao de matrizes (ordem dos lacos) ===");
        int n = 400;
        int[][] a = matrizAleatoria(n, n);
        int[][] b = matrizAleatoria(n, n);

        long inicioIJK = System.nanoTime();
        int[][] resultadoIJK = multiplicarIJK(a, b);
        long tempoIJK = System.nanoTime() - inicioIJK;

        long inicioIKJ = System.nanoTime();
        int[][] resultadoIKJ = multiplicarIKJ(a, b);
        long tempoIKJ = System.nanoTime() - inicioIKJ;

        boolean iguais = java.util.Arrays.deepEquals(resultadoIJK, resultadoIKJ);

        double msIJK = tempoIJK / 1_000_000.0;
        double msIKJ = tempoIKJ / 1_000_000.0;

        System.out.println("Tamanho da matriz: " + n + "x" + n);
        System.out.println("Ordem ijk: " + msIJK + " ms");
        System.out.println("Ordem ikj: " + msIKJ + " ms");
        System.out.println("Fator observado (ijk / ikj): " + (msIJK / msIKJ));
        System.out.println("Resultados iguais: " + iguais);
    }
}

// matriz esparsa
// implementar a representacao por triplas (linha, coluna, valor)
// com leitura, escrita e percurso dos elementos nao nulos
class MatrizEsparsa {

    private static class Tripla {
        int linha, coluna, valor;

        Tripla(int linha, int coluna, int valor) {
            this.linha = linha;
            this.coluna = coluna;
            this.valor = valor;
        }
    }

    private final int linhas;
    private final int colunas;
    private final java.util.List<Tripla> triplas = new java.util.ArrayList<>();

    MatrizEsparsa(int linhas, int colunas) {
        this.linhas = linhas;
        this.colunas = colunas;
    }

    private void validar(int i, int j) {
        if (i < 0 || i >= linhas || j < 0 || j >= colunas) {
            throw new IndexOutOfBoundsException("posicao (" + i + "," + j + ") fora da matriz " + linhas + "x" + colunas);
        }
    }

    // escrita: define o valor na posicao (i, j)
    void set(int i, int j, int valor) {
        validar(i, j);
        for (Tripla t : triplas) {
            if (t.linha == i && t.coluna == j) {
                if (valor == 0) {
                    triplas.remove(t);
                } else {
                    t.valor = valor;
                }
                return;
            }
        }
        if (valor != 0) {
            triplas.add(new Tripla(i, j, valor));
        }
    }

    // leitura: retorna o valor na posicao (i, j), 0 se nao existir
    int get(int i, int j) {
        validar(i, j);
        for (Tripla t : triplas) {
            if (t.linha == i && t.coluna == j) {
                return t.valor;
            }
        }
        return 0;
    }

    int quantidadeNaoNulos() {
        return triplas.size();
    }

    // percurso dos elementos nao nulos
    void percorrerNaoNulos() {
        for (Tripla t : triplas) {
            System.out.println("(" + t.linha + ", " + t.coluna + ") = " + t.valor);
        }
    }

    static void executar() {
        System.out.println("=== Matriz esparsa (representacao por triplas) ===");
        MatrizEsparsa m = new MatrizEsparsa(5, 5);
        m.set(0, 0, 3);
        m.set(1, 3, 7);
        m.set(4, 4, 9);
        m.set(1, 3, 0); // remove o elemento

        System.out.println("Elementos nao nulos: " + m.quantidadeNaoNulos());
        m.percorrerNaoNulos();

        System.out.println("get(0,0) = " + m.get(0, 0));
        System.out.println("get(1,3) = " + m.get(1, 3));
        System.out.println("get(2,2) = " + m.get(2, 2));
    }
}

// medir memoria e tempo das duas representacoes (densa x esparsa)
// e dizer a partir de qual densidade a esparsa deixa de valer a pena
class DensidadeComparacao {

    static final int N = 500; // matriz N x N
    static final int BYTES_POR_INT = 4;
    static final double[] DENSIDADES = { 0.01, 0.02, 0.05, 0.10, 0.20, 0.30, 1.0 / 3.0, 0.40, 0.50, 0.70, 1.0 };

    static void executar() {
        System.out.println("=== Densidade: densa x esparsa (memoria e tempo) ===");
        java.util.Random rand = new java.util.Random(42);
        long memDensa = (long) N * N * BYTES_POR_INT;

        System.out.printf("%-10s %-10s %-14s %-14s %-16s %-18s %-16s %-18s%n",
                "densidade", "nnz", "memDensa(B)", "memEsparsa(B)",
                "buildDensa(ms)", "buildEsparsa(ms)", "somaDensa(ms)", "somaEsparsa(ms)");

        for (double densidade : DENSIDADES) {
            int nnz = (int) (N * (long) N * densidade);

            // gera nnz posicoes distintas (linha*N + coluna) e seus valores
            java.util.Set<Integer> posicoes = new java.util.HashSet<>();
            while (posicoes.size() < nnz) {
                posicoes.add(rand.nextInt(N * N));
            }
            int[] linha = new int[nnz];
            int[] coluna = new int[nnz];
            int[] valor = new int[nnz];
            int idx = 0;
            for (int pos : posicoes) {
                linha[idx] = pos / N;
                coluna[idx] = pos % N;
                valor[idx] = 1 + rand.nextInt(9);
                idx++;
            }

            // construcao da representacao densa
            long inicio = System.nanoTime();
            int[][] densa = new int[N][N];
            for (int k = 0; k < nnz; k++) {
                densa[linha[k]][coluna[k]] = valor[k];
            }
            long buildDensa = System.nanoTime() - inicio;

            // construcao da representacao esparsa (ja gerada acima; mede so a copia)
            inicio = System.nanoTime();
            int[] linhaEsparsa = linha.clone();
            int[] colunaEsparsa = coluna.clone();
            int[] valorEsparsa = valor.clone();
            long buildEsparsa = System.nanoTime() - inicio;
            // linha/colunaEsparsa fazem parte da tripla completa (usadas em get/set reais);
            // aqui so a soma dos valores e medida, entao validamos o tamanho para nao ficarem sem uso
            if (linhaEsparsa.length != nnz || colunaEsparsa.length != nnz) {
                throw new IllegalStateException("tamanho inconsistente na representacao esparsa");
            }

            // percurso completo (soma de todos os elementos)
            inicio = System.nanoTime();
            long somaDensaVal = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    somaDensaVal += densa[i][j];
                }
            }
            long somaDensa = System.nanoTime() - inicio;

            inicio = System.nanoTime();
            long somaEsparsaVal = 0;
            for (int k = 0; k < nnz; k++) {
                somaEsparsaVal += valorEsparsa[k];
            }
            long somaEsparsa = System.nanoTime() - inicio;

            long memEsparsa = (long) nnz * 3 * BYTES_POR_INT;

            System.out.printf("%-10.4f %-10d %-14d %-14d %-16.3f %-18.3f %-16.3f %-18.3f%n",
                    densidade, nnz, memDensa, memEsparsa,
                    buildDensa / 1_000_000.0, buildEsparsa / 1_000_000.0,
                    somaDensa / 1_000_000.0, somaEsparsa / 1_000_000.0);

            if (somaDensaVal != somaEsparsaVal) {
                throw new IllegalStateException("somas divergentes, bug na comparacao");
            }
        }

        double limiar = (double) BYTES_POR_INT / (3 * BYTES_POR_INT); // memEsparsa == memDensa
        System.out.println();
        System.out.println("Cada elemento denso custa " + BYTES_POR_INT + " bytes (um int).");
        System.out.println("Cada elemento esparso custa " + (3 * BYTES_POR_INT) + " bytes (linha, coluna, valor).");
        System.out.printf("Em memoria, a esparsa deixa de valer a pena quando densidade > %.4f (%.1f%%),%n", limiar, limiar * 100);
        System.out.println("pois nesse ponto nnz * 3 ints passa a ocupar mais espaco que os N*N ints da matriz densa.");
        System.out.println("Em tempo de percurso, a esparsa so varre os nnz elementos, entao continua mais rapida");
        System.out.println("mesmo em densidades onde ja perdeu a vantagem de memoria.");
    }
}
