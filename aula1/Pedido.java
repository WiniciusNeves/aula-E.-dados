package aula1;

/**
 * Pedido
 */
public class Pedido {
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
