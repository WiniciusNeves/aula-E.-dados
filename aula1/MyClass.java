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

       
    }
}
