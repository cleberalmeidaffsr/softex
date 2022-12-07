import './App.css'
import OlaMundo from './componentes/OlaMundo'
import SayMyName from './componentes/SayMyName'
import Pessoa from './componentes/Pessoa'

function App() {

  const nome = 'maria'

  return (
    <div className="App">
      <OlaMundo/>
      <SayMyName nome='cleber' />
      <SayMyName nome='Jão' />
      <SayMyName nome={nome} />

      <Pessoa
        nome='Cleber'
        idade='19 anos'
        profissao='estudante'
        foto='https://via.placeholder.com/150'
      />

    </div>
  );
}

export default App;
