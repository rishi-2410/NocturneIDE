# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2025 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a writer for open search engine descriptions.
"""

from PyQt6.QtCore import QIODevice, QXmlStreamWriter


class OpenSearchWriter(QXmlStreamWriter):
    """
    Class implementing a writer for open search engine descriptions.
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()

        self.setAutoFormatting(True)

    def write(self, device, engine):
        """
        Public method to write the description of an engine.

        @param device reference to the device to write to
        @type QIODevice
        @param engine reference to the engine
        @type OpenSearchEngine
        @return flag indicating success
        @rtype bool
        """
        if engine is None:
            return False

        if not device.isOpen() and not device.open(QIODevice.OpenModeFlag.WriteOnly):
            return False

        self.setDevice(device)
        self.__write(engine)
        return True

    def __write(self, engine):
        """
        Private method to write the description of an engine.

        @param engine reference to the engine
        @type OpenSearchEngine
        """
        self.writeStartDocument()
        self.writeStartElement("OpenSearchDescription")
        self.writeDefaultNamespace("http://a9.com/-/spec/opensearch/1.1/")

        if engine.name():
            self.writeTextElement("ShortName", engine.name())

        if engine.description():
            self.writeTextElement("Description", engine.description())

        if engine.searchUrlTemplate():
            self.writeStartElement("Url")
            self.writeAttribute("method", engine.searchMethod())
            self.writeAttribute("type", "text/html")
            self.writeAttribute("template", engine.searchUrlTemplate())

            if len(engine.searchParameters()) > 0:
                self.writeNamespace(
                    "http://a9.com/-/spec/opensearch/extensions/parameters/1.0/", "p"
                )
                for parameter in engine.searchParameters():
                    self.writeStartElement("p:Parameter")
                    self.writeAttribute("name", parameter[0])
                    self.writeAttribute("value", parameter[1])

            self.writeEndElement()

        if engine.suggestionsUrlTemplate():
            self.writeStartElement("Url")
            self.writeAttribute("method", engine.suggestionsMethod())
            self.writeAttribute("type", "application/x-suggestions+json")
            self.writeAttribute("template", engine.suggestionsUrlTemplate())

            if len(engine.suggestionsParameters()) > 0:
                self.writeNamespace(
                    "http://a9.com/-/spec/opensearch/extensions/parameters/1.0/", "p"
                )
                for parameter in engine.suggestionsParameters():
                    self.writeStartElement("p:Parameter")
                    self.writeAttribute("name", parameter[0])
                    self.writeAttribute("value", parameter[1])

            self.writeEndElement()

        if engine.imageUrl():
            self.writeTextElement("Image", engine.imageUrl())

        self.writeEndElement()
        self.writeEndDocument()
