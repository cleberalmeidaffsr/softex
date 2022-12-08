function Evento({ numero }) {

    function meuEvento() {
        console.log(`Fui ativado! ${numero}`)
    }

    return (
        <>
            <p>Clique para disparar um evento:</p>
            <button onClick={meuEvento}>Ative</button>
        </>
    )
}

export default Evento