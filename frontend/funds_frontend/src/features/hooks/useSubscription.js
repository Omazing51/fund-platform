import { useEffect, useState } from "react";
import { getAllSubscription, deleteSubscription } from "../services/subscriptionService";

export function useSubscriptions() {
  const [subscriptions, setSubscriptions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchSubscriptions() {
      try {
        setLoading(true);
        const data = await getAllSubscription();
        setSubscriptions(data || []);
      } catch (err) {
        setError("Error al cargar las suscripciones");
      } finally {
        setLoading(false);
      }
    }
    fetchSubscriptions();
  }, []);

async function removeSubscription(fundId) {
  try {
    await deleteSubscription(fundId);
    setSubscriptions(prev => prev.filter(s => s.FundId !== fundId));
  } catch (error) {
    console.error("Error eliminando suscripción", error);
  }
}

  return { subscriptions, loading, error, removeSubscription };
}
