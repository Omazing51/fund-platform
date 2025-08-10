import FundCard from "./FundCard";

export default function FundsList({ funds, onSubscribed }) {
  if (!funds.length) {
    return <p>No hay fondos disponibles.</p>;
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {funds.map((fund) => (
        <FundCard key={fund.FundId} fund={fund} onSubscribed={onSubscribed} />
      ))}
    </div>
  );
}
