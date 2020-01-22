import React from 'react';
import List from '../common/List';

interface State {
    news: any[];
}

class GamingPage extends React.PureComponent<{}, State> {
    constructor(props: {}) {
        super(props);
        this.state = {
            news: ['news1', 'news2'],
        };
    }

    render(): React.ReactNode {
        const { news } = this.state;
        return (
            <article className="gaming-page">
                <List title="Gaming News" items={news} />
                <button type="button">Back</button>
            </article>
        );
    }
}

export default GamingPage;
