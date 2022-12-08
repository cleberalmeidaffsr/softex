import { BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import Footer from './componentes/layout/Footer';
import NavBar from './componentes/layout/NavBar';
import Contato from './paginas/Contato';
import Empresa from './paginas/Empresa';
import Home from './paginas/Home';

function App() {

  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path='/' exact='true' element={<Home />}></Route>
        <Route path='/contato' element={<Contato />}></Route>
        <Route path='/empresa' element={<Empresa />}></Route>
      </Routes>
      <Footer/>
    </Router>
  )
}

export default App;
