import java.io.Serializable;

public class Aluno implements Serializable {
    private String nome;
    private String senha;
    private String endereco;

    public Aluno(String nome, String senha, String endereco) {
        this.setNome(nome);
        this.setSenha(senha);
        this.setEndereco(endereco);
    }

    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public String getSenha(){
        return senha;
    }

    public void setSenha(String senha){
        this.senha = senha;
    }

    public String getEndereco(){
        return endereco;
    }
    
    public void setEndereco(String nomeCurso){
        this.endereco = nomeCurso;
    }
}