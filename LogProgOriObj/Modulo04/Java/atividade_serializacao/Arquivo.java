import java.io.*;

public class Arquivo {
    public static void main(String[] args) throws Exception {
        arquivoSerializacao();
        leituraserializacao();
   }

   private static void arquivoSerializacao(){
        Aluno p1 = new Aluno("Cleber de Almeida","123456", "Rua Marques de Rui Lopez");
        FileOutputStream fos = null;
        ObjectOutputStream oos = null;
        try{
            fos = new FileOutputStream("arquivo.bin");
            oos = new ObjectOutputStream(fos);
            oos.writeObject(p1);
        }catch(FileNotFoundException e){
            System.out.println("Arquivo Não Encontrado.");
        }catch(IOException e){
            System.out.println("Erro ao criar Arquivo");
        }finally{
            try{
                oos.close();
            }catch (IOException e){
                System.out.println("Erro ao Fechar o Arquivo");
            }
        }
    }

    private static void leituraserializacao(){
        Aluno a1 = null;
        FileInputStream fis = null;
        ObjectInputStream ois = null;
        try{
            fis = new FileInputStream("arquivo.bin");
            ois = new ObjectInputStream(fis);
            a1 = (Aluno)ois.readObject();
            System.out.printf("Nome: %s \n Senha: %s \n Endereço: %s \n", a1.getNome(), a1.getSenha(), a1.getEndereco());
        }catch(ClassNotFoundException e){
            System.out.println("Classe Não Encontrado.");
        }catch(IOException e){
            System.out.println("Erro ao criar Arquivo");
        }finally{
            try{
                ois.close();
            }catch (IOException e){
                System.out.println("Erro ao Fechar o Arquivo");
            }
        }
    }
}
