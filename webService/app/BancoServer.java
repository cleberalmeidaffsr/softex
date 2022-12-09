package webService.app;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;

@webService
@SOAPBinding(style = Style.RPC)
public interface BancoServer {
    @WebMethod String pegarBoleto(String codigoBarras);
    @WebMethod String criarBoleto(Float valor ,String cpfCliente);
    @WebMethod boolean verificarPagamento(String codigoBarras);
    @WebMethod boolean cancelarBoleto(String codigoBarras);
}
