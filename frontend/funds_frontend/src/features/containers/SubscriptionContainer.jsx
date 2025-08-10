import { useSubscriptions } from "../hooks/useSubscription";
import SubscriptionsList from "../components/SubscriptionsList";

export default function SubscriptionContainer() {
  const { subscriptions, loading, error, removeSubscription } = useSubscriptions();

  if (loading) return <p>Cargando fondos...</p>;
  if (error) return <p>{error}</p>;

  return (
    <SubscriptionsList
      subscriptions={subscriptions}
      onDelete={removeSubscription}
    />
  );
}
