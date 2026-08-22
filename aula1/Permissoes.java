package aula1;

// Permissões representadas como um único int, um bit por permissão.
public class Permissoes {

    public static final int LER      = 1 << 0; // 00001
    public static final int ESCREVER = 1 << 1; // 00010
    public static final int EXECUTAR = 1 << 2; // 00100
    public static final int DELETAR  = 1 << 3; // 01000
    public static final int ADMIN    = 1 << 4; // 10000

    private static final String[] NOMES   = {"LER", "ESCREVER", "EXECUTAR", "DELETAR", "ADMIN"};
    private static final int[]    VALORES = {LER, ESCREVER, EXECUTAR, DELETAR, ADMIN};

    public static int conceder(int permissoes, int permissao) {
        return permissoes | permissao;
    }

    public static int revogar(int permissoes, int permissao) {
        return permissoes & ~permissao;
    }

    public static int alternar(int permissoes, int permissao) {
        return permissoes ^ permissao;
    }

    public static boolean testar(int permissoes, int permissao) {
        return (permissoes & permissao) == permissao;
    }

    public static String listar(int permissoes) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < NOMES.length; i++) {
            if (testar(permissoes, VALORES[i])) {
                if (sb.length() > 0) sb.append(", ");
                sb.append(NOMES[i]);
            }
        }
        return sb.length() == 0 ? "(nenhuma)" : sb.toString();
    }

    public static void main(String[] args) {
        int p = 0;
        System.out.println("Inicial: " + listar(p));

        p = conceder(p, LER);
        p = conceder(p, EXECUTAR);
        System.out.println("Após conceder LER e EXECUTAR: " + listar(p));

        p = revogar(p, LER);
        System.out.println("Após revogar LER: " + listar(p));

        p = alternar(p, ESCREVER);
        System.out.println("Após alternar ESCREVER (liga): " + listar(p));
        p = alternar(p, ESCREVER);
        System.out.println("Após alternar ESCREVER de novo (desliga): " + listar(p));

        p = conceder(p, ADMIN);
        System.out.println("Após conceder ADMIN: " + listar(p));

        System.out.println("Tem EXECUTAR? " + testar(p, EXECUTAR));
        System.out.println("Tem DELETAR? " + testar(p, DELETAR));

        // Conceder LER e EXECUTAR de uma vez só, combinando as flags com OR
        int q = conceder(0, LER | EXECUTAR);
        System.out.println("q (LER | EXECUTAR de uma vez): " + listar(q));
    }
}
