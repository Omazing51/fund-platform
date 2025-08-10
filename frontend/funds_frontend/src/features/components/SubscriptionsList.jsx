import SubscriptionCard from "./SubscriptionCard";

export default function SubscriptionsList({ subscriptions, onDelete }) {
  if (!subscriptions.length) {
    return <p>No tienes suscripciones disponibles.</p>;
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {subscriptions.map((subscription, index) => (
        <SubscriptionCard
          key={subscription.SubscriptionId || index}
          subscription={subscription}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
}
