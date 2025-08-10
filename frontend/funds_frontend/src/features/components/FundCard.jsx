export default function FundCard({ fund }) {
  return (
    <div className="bg-white p-6 shadow-lg rounded-lg">
      <h2 className="text-xl font-bold">{fund.Name}</h2>
      <p>Monto: ${fund.MinAmount}</p>
      <button className="bg-red-400 text-md font-bold rounded-sm p-2 mt-2">
        Eliminar fondo
      </button>
    </div>
  );
}
