export default function SubscriptionCard({ subscription, onDelete }) {
  return (
    <div className="bg-white p-6 shadow-lg rounded-lg">
      <h2 className="text-xl font-bold">{subscription.AccountId}</h2>
      <p>Código del fondo: {subscription.FundId}</p>
      <button
        className="bg-red-400 text-md font-bold rounded-sm p-2 mt-2"
         onClick={() => onDelete(subscription.FundId)}
      >
        Eliminar fondo
      </button>
    </div>
  );
}
