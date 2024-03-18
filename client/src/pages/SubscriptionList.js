import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";

function SubscriptionList() {

    const [subscriptions, setsubScriptions] = useState([]);

    useEffect(() => {
        fetch('/subscriptions')
            .then((r) => r.json())
            .then(setsubScriptions);
    }, []);

    return (
        <Wrapper>
            {subscriptions.length > 0 ? (
                subscriptions.map((sub) => (
                    <sub key={sub.id}>
                        <div>
                            <h2>{sub.type}</h2>
                            <p>
                                <div>{sub.sub_price}</div>
                                {sub.description}
                            </p>
                        </div>
                    </sub>
                ))
            ) : (
                <>
                    <h2> No Subscriptions found</h2>
                </>
            )}
        </Wrapper>
    );
}

const Wrapper = styled.section`
    max-width: 800px;
    margin: 40px auto;
`;

const Recipe = styled.article`
    margin-bottom: 240px;
`;

export default SubscriptionList