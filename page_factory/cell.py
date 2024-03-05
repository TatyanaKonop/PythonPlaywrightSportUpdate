from page_factory.component import Component


class Cell(Component):
    @property
    def type_of(self) -> str:
        return 'cell'
