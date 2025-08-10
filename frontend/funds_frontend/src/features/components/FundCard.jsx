import { useState } from "react";
import { createSubscription } from "../services/subscriptionService";

export default function FundCard({ fund, onSubscribed }) {
  const [notificationType, setNotificationType] = useState("");
  const [message, setMessage] = useState("");

  const handleSubscribe = () => {
    if (!notificationType) {
      setMessage("Selecciona un método de notificación");
      return;
    }

    createSubscription(fund.FundId, notificationType)
      .then(() => {
        setMessage("Suscripción creada correctamente");
        if (onSubscribed) onSubscribed();
      })
      .catch((err) => {
        console.error(err);
        setMessage("Error al crear la suscripción");
      });
  };

  return (
    <div className="bg-white p-6 shadow-lg rounded-lg">
      <h2 className="text-xl font-bold">{fund.Name}</h2>
      <p>Monto: ${fund.MinAmount}</p>

      <select
        value={notificationType}
        onChange={(e) => setNotificationType(e.target.value)}
        className="border rounded p-2 mt-3 w-full"
      >
        <option value="">Seleccionar notificación...</option>
        <option value="email">Email</option>
        <option value="sms">SMS</option>
      </select>

      <button
        onClick={handleSubscribe}
        className="bg-green-400 text-md font-bold rounded-sm p-2 mt-3 w-full hover:bg-green-500"
      >
        Suscribirse al fondo
      </button>

      {message && <p className="mt-2 text-sm">{message}</p>}
    </div>
  );
}
