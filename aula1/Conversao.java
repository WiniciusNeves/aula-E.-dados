package aula1;

// Conversão decimal -> binário e decimal -> hexadecimal, 32 bits com sinal.
// Negativos são tratados em complemento de dois, exatamente como o int já
// é representado na memória: por isso a conversão é feita bit a bit com
// deslocamento sem sinal (>>>), sem nunca calcular o valor absoluto.
public class Conversao {

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

    public static void main(String[] args) {
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
