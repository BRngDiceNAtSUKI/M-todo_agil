package src;

public class div {

    public static double calcular(double a, double b) {
        if (b == 0) {
            throw new IllegalArgumentException("Não pode dividir por zero");
        }

        return a / b;
    }

    public static void main(String[] args) {

        // teste 1
        assert calcular(10, 5) == 2;

        // teste 2
        assert calcular(6, 3) == 2;

        // teste 3
        try {
            calcular(10, 0);
            assert false;
        } catch (IllegalArgumentException e) {
            assert true;
        }

        System.out.println("Todos os testes passaram!");
    }
}
