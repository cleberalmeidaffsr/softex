package LogProgOriObj.Modulo04.Java.atividade_excesao;

public class excecao {
    public static void main(String[] args) {
        try {
            int[] a = {1, 2, 3};
            System.out.println(a[0]);

        } catch(ArrayIndexOutOfBoundsException e) {
            System.out.println("Seu indicie está fora do limite do array");

        } catch(Exception e) {
            System.out.println("Seu código está errado.");
        }
    }
}
