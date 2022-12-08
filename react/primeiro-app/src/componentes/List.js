import Item from "./Item"

function List () {
    return (
        <>
            <h1>Minha Lista</h1>
            <ul>
                <Item marca="Ferrari" anoLancamento={1982} />
                <Item marca="Mercedes" anoLancamento={1965} />
                <Item marca="Fiat" />
                <Item marca="Renault"  />
                <Item />
            </ul>
        </>
    )
}

export default List