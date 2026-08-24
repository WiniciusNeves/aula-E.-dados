package aula1;

// tranforme 37 em binario
// 1101 0110 para decimais
// 200 em hexadecimaldo

// reescreva sem o nao externo
//if (!(idade >= 18&& temDocumento))
//if (!(pedido == null || pedido.getItems().isEmpty() ))
// while (!(fim || erro))

// p = 1 quais permissões estao ativas
// p = 7 o que faz p &= ~2
// como conceder ler e executar, de um vez so

public class MyClass {
    public static void main(String[] args) {
        int decimal = 37;
        String binary = Integer.toBinaryString(decimal);
        System.out.println("Decimal: " + decimal + " em binário: " + binary);

        String binaryInput = "11010110";
        int decimalFromBinary = Integer.parseInt(binaryInput, 2);
        System.out.println("Binário: " + binaryInput + " em decimal: " + decimalFromBinary);

        int hexDecimal = 200;
        String hex = Integer.toHexString(hexDecimal);
        System.out.println("Decimal: " + hexDecimal + " em hexadecimal: " + hex);


        // Reescrevendo as expressões sem o "não" externo
        int idade = 20;
        boolean temDocumento = true;
        Pedido pedido = null;

        boolean fim = true;
        boolean erro = false;

        while (fim && erro) {
            // Lógica do loop
        }

        if (idade < 18 || !temDocumento) return;

        if (!(pedido != null && pedido.getItems().length > 0)) return;

        // Permissões
        int p = 1; // Permissões ativas
        System.out.println("Permissões ativas: " + p);
        p = 7; // Permissões ativas
        System.out.println("Permissões ativas: " + p);
        p &= ~2; // Remove a permissão 2
        System.out.println("Permissões após remover a permissão 2: " + p);
        p |= 4; // Concede a permissão 4
        System.out.println("Permissões após conceder a permissão 4: " + p);
        p |= 1; // Concede a permissão 1
        System.out.println("Permissões depois de conceder a permissão 1: " + p);

        System.out.println();
        Conversao.demonstrar();

        System.out.println();
        Permissoes.demonstrar();
    }
}

// Conversão decimal -> binário e decimal -> hexadecimal, 32 bits com sinal.
// Negativos são tratados em complemento de dois, exatamente como o int já
// é representado na memória: por isso a conversão é feita bit a bit com
// deslocamento sem sinal (>>>), sem nunca calcular o valor absoluto.
class Conversao {

    public static String paraBinario(int n) {
        StringBuilder sb = new StringBuilder(32);
        for (int i = 31; i >= 0; i--) {
            sb.append((n >>> i) & 1);
        }
        return sb.toString();
    }

    public static String paraHexadecimal(int n) {
        char[] digitos = "0123456789ABCDEF".toCharArray();
        StringBuilder sb = new StringBuilder(8);
        for (int i = 7; i >= 0; i--) {
            int nibble = (n >>> (i * 4)) & 0xF;
            sb.append(digitos[nibble]);
        }
        return sb.toString();
    }

    // Preenche com zeros à esquerda até 'tamanho' para comparar com a biblioteca,
    // que não faz esse padding para números positivos.
    private static String pad(String s, int tamanho) {
        StringBuilder sb = new StringBuilder();
        for (int i = s.length(); i < tamanho; i++) sb.append('0');
        return sb.append(s).toString();
    }

    public static void demonstrar() {
        int[] testes = {37, -37, 0, -1, Integer.MAX_VALUE, Integer.MIN_VALUE};

        for (int n : testes) {
            String bin = paraBinario(n);
            String hex = paraHexadecimal(n);
            String binLib = pad(Integer.toBinaryString(n), 32);
            String hexLib = pad(Integer.toHexString(n), 8).toUpperCase();

            System.out.println("n = " + n);
            System.out.println("  meu bin: " + bin + (bin.equals(binLib) ? "  (igual à lib)" : "  (DIVERGIU: " + binLib + ")"));
            System.out.println("  meu hex: " + hex + (hex.equals(hexLib) ? "  (igual à lib)" : "  (DIVERGIU: " + hexLib + ")"));
        }
    }
}

/**
 * Pedido
 */
class Pedido {
    private String id;
    private String cliente;
    private String[] items;

    public Pedido(String id, String cliente, String[] items) {
        this.id = id;
        this.cliente = cliente;
        this.items = items;
    }

    public String getId() {
        return id;
    }

    public String getCliente() {
        return cliente;
    }

    public String[] getItems() {
        return items;
    }
}

// Permissões representadas como um único int, um bit por permissão.
class Permissoes {

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

    public static void demonstrar() {
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
