package webService.app;

import java.util.Date;
import javax.jws.WebService;

@WebService(endpointInterface = "app.BancoServer")

public class BancoServerImpl implements BancoServer {

    public String pegarBoleto(String codigoBarras) {
        return "Boleto para o código " + codigoBarras;
    }

    public String criarBoleto(float valor, String cpfCliente) {
        return "123.123.123-42";
    }

    public boolean verificarPagamento(String codigoBarras) {
        return true;
    }

    public boolean cancelarBoleto(String codigoBarras) {
        return false;
    }
    
}
