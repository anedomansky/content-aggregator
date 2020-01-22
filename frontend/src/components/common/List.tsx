import React from 'react';

interface Props {
    title: string;
    items: any[];
}

const List: React.FC<Props> = ({ title, items }) => (
    <article className="list">
        <h1 className="list__title">{title}</h1>
        <ul>
            {items.map((item: any, index: number) => (
                <li key={index}>{item}</li>
            ))}
        </ul>
    </article>
);

export default List;
