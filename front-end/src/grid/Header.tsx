import headersData from "../dummy_data/headers.json"

export default function Header() {
    return (
        <div className="grid grid-flow-col justify-between">
            {headersData.map((value : string, index : number) => (
                <div key={index}>
                    {value}: {index}
                </div>
            ))}
        </div>
    )
}